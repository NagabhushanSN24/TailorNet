import os
import numpy as np
import torch

from psbody.mesh import Mesh

from models.tailornet_model import get_best_runner as get_tn_runner
from models.torch_smpl4garment import TorchSMPL4Garment as SMPL4Garment
from utils.rotation import normalize_y_rotation
from visualization.blender_renderer import visualize_garment_body

from dataset.canonical_pose_dataset import get_style, get_shape
from visualization.vis_utils import get_specific_pose, get_specific_style_old_tshirt
from visualization.vis_utils import get_specific_shape, get_amass_sequence_thetas
from utils.interpenetration import remove_interpenetration_fast

# Set output path where inference results will be stored
OUT_PATH = "/mnt/zfs/ml-ab-team/nagabhushan/01_SizeBasedTryOn/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0005"


def get_single_frame_inputs(garment_class, gender):
    """Prepare some individual frame inputs."""
    betas = [
        get_specific_shape('mean'),
        get_specific_shape('mean'),
        get_specific_shape('mean'),
        get_specific_shape('mean'),
        get_specific_shape('mean'),
    ]
    # old t-shirt style parameters are centered around [1.5, 0.5, 1.5, 0.0]
    # whereas all other garments styles are centered around [0, 0, 0, 0]
    if garment_class == 'old-t-shirt':
        gammas = [
            get_specific_style_old_tshirt('mean'),
            get_specific_style_old_tshirt('big'),
            get_specific_style_old_tshirt('small'),
            get_specific_style_old_tshirt('shortsleeve'),
            get_specific_style_old_tshirt('big_shortsleeve'),
        ]
    else:
        gammas = [
            get_style('000', garment_class=garment_class, gender=gender),
            get_style('001', garment_class=garment_class, gender=gender),
            get_style('002', garment_class=garment_class, gender=gender),
            get_style('003', garment_class=garment_class, gender=gender),
            get_style('004', garment_class=garment_class, gender=gender),
        ]
    thetas = [
        get_specific_pose(0),
        get_specific_pose(0),
        get_specific_pose(0),
        get_specific_pose(0),
        get_specific_pose(0),
    ]
    return thetas, betas, gammas


def get_sequence_inputs(garment_class, gender):
    """Prepare sequence inputs."""
    beta = get_specific_shape('somethin')
    if garment_class == 'old-t-shirt':
        gamma = get_specific_style_old_tshirt('big_longsleeve')
    else:
        gamma = get_style('000', gender=gender, garment_class=garment_class)

    # downsample sequence frames by 2
    thetas = get_amass_sequence_thetas('05_02')[::2]

    betas = np.tile(beta[None, :], [thetas.shape[0], 1])
    gammas = np.tile(gamma[None, :], [thetas.shape[0], 1])
    return thetas, betas, gammas


def run_tailornet():
    gender = 'female'
    garment_class = 'short-pant'
    thetas, betas, gammas = get_single_frame_inputs(garment_class, gender)
    # # uncomment the line below to run inference on sequence data
    # thetas, betas, gammas = get_sequence_inputs(garment_class, gender)

    # load model
    tn_runner = get_tn_runner(gender=gender, garment_class=garment_class)
    # from trainer.base_trainer import get_best_runner
    # tn_runner = get_best_runner("/BS/cpatel/work/data/learn_anim/tn_baseline/{}_{}/".format(garment_class, gender))
    smpl = SMPL4Garment(gender=gender)

    # make out directory if doesn't exist
    if not os.path.isdir(OUT_PATH):
        os.mkdir(OUT_PATH)

    # run inference
    for i, (theta, beta, gamma) in enumerate(zip(thetas, betas, gammas)):
        print(i, len(thetas))
        # normalize y-rotation to make it front facing
        theta_normalized = normalize_y_rotation(theta)
        theta = torch.from_numpy(theta.astype(np.float32)).cuda()
        theta_normalized = torch.from_numpy(theta_normalized.astype(np.float32)).cuda()
        beta = torch.from_numpy(beta.astype(np.float32)).cuda()
        gamma = torch.from_numpy(gamma.astype(np.float32)).cuda()
        with torch.no_grad():
            pred_verts_d = tn_runner.forward(
                thetas=theta_normalized[None, :],
                betas=beta[None, :],
                gammas=gamma[None, :],
            )[0].cuda()

        # get garment from predicted displacements
        body, pred_gar, body_gar = smpl(beta=beta, theta=theta, garment_class=garment_class, garment_d=pred_verts_d)
        pred_gar = remove_interpenetration_fast(pred_gar, body)

        np.save(f'vertices_{gender}_{garment_class}_{i:02}_garment.npy', pred_gar.v)
        np.save(f'vertices_{gender}_{garment_class}_{i:02}_body_garment.npy', body_gar.v)

        # save body and predicted garment
        body.write_ply(os.path.join(OUT_PATH, "body_{:04d}.ply".format(i)))
        pred_gar.write_ply(os.path.join(OUT_PATH, "pred_gar_{:04d}.ply".format(i)))


def render_images():
    """Render garment and body using blender."""
    i = 0
    while True:
        body_path = os.path.join(OUT_PATH, "body_{:04d}.ply".format(i))
        if not os.path.exists(body_path):
            break
        body = Mesh(filename=body_path)
        pred_gar = Mesh(filename=os.path.join(OUT_PATH, "pred_gar_{:04d}.ply".format(i)))

        visualize_garment_body(
            pred_gar, body, os.path.join(OUT_PATH, "img_{:04d}.png".format(i)), garment_class='t-shirt', side='front')
        i += 1

    # Concate frames of sequence data using this command
    # ffmpeg -r 10 -i img_%04d.png -vcodec libx264 -crf 10  -pix_fmt yuv420p check.mp4
    # Make GIF
    # convert -delay 200 -loop 0 -dispose 2 *.png check.gif
    # convert check.gif -resize 512x512 check_small.gif


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == 'inference':
        run_tailornet()
    elif sys.argv[1] == 'render':
        render_images()
    else:
        raise AttributeError
