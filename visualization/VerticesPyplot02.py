# 

import datetime
import time
import traceback

from pathlib import Path
import numpy
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

this_filepath = Path(__file__)
this_filename = this_filepath.stem


def find_closest_vertices(x: numpy.ndarray):
    top_vertex_indices = [591, 593, 594, 2390, 2391, 2393, 2397, 2398, 2402, 2403]
    bottom_vertex_indices = [1023, 1022, 970, 971, 972, 973, 974, 2075, 2020, 2019, 2021, 2022]

    top_vertices = x[top_vertex_indices]
    bottom_vertices = x[bottom_vertex_indices]

    remove_length_axis = lambda array: numpy.stack([array[:, 0], array[:, 2]], axis=1)

    top_vertices_xy = remove_length_axis(top_vertices)
    bottom_vertices_xy = remove_length_axis(bottom_vertices)

    distances = numpy.linalg.norm(top_vertices_xy[:, None] - bottom_vertices_xy[None], ord=2, axis=2)
    top_vertex_id, bottom_vertex_id = numpy.unravel_index(distances.argmin(), distances.shape)
    top_vertex_index = top_vertex_indices[top_vertex_id]
    bottom_vertex_index = bottom_vertex_indices[bottom_vertex_id]

    print(f'top vertex index: {top_vertex_index}; top_vertex: {x[top_vertex_index]}')
    print(f'bottom vertex index: {bottom_vertex_index}; bottom_vertex: {x[bottom_vertex_index]}')
    print(f'length: {x[top_vertex_index][1] - x[bottom_vertex_index][1]}')
    return


def main():
    show_vertex_index = True

    vertices_body01 = numpy.load(
        '/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0004/model_data/vertices_body01.npy')
    vertices_body02 = numpy.load(
        '/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0004/model_data/vertices_body02.npy')
    vertices_body03 = numpy.load(
        '/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0004/model_data/vertices_body03.npy')
    vertices_cloth01 = numpy.load(
        '/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0004/model_data/vertices_cloth01.npy')
    vertices_cloth02 = numpy.load(
        '/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0004/model_data/vertices_cloth02.npy')
    faces_body = numpy.load(
        '/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0004/model_data/faces_body.npy')
    faces_cloth = numpy.load(
        '/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0004/model_data/faces_cloth.npy')
    mesh = numpy.load(
        '/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0004/model_data/mesh_vertices.npy')

    find_closest_vertices(vertices_cloth01)

    fig = pyplot.figure()
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(222, projection='3d')
    ax3 = fig.add_subplot(224, projection='3d')

    # Plot the scatter plots
    x = vertices_body02
    y = vertices_cloth01
    z = vertices_cloth02
    scatter1 = ax1.scatter(x[:, 0], x[:, 1], x[:, 2], c='r')
    scatter2 = ax2.scatter(y[:, 0], y[:, 1], y[:, 2], c='g')
    scatter3 = ax3.scatter(z[:, 0], z[:, 1], z[:, 2], c='b')
    if show_vertex_index:
        for i in range(x.shape[0]):
            # if i not in [591, 593, 594, 2390, 2391, 2393, 2397, 2398, 2402, 2403]:
            #     continue
            # if i not in [1023, 1022, 970, 971, 972, 973, 974, 2075, 2020, 2019, 2021, 2022]:
            #     continue
            if i not in [2390, 2022]:
                continue
            ax1.text(x[i, 0], x[i, 1], x[i, 2], str(i), fontsize=8, color='r', ha='right')
            ax2.text(y[i, 0], y[i, 1], y[i, 2], str(i), fontsize=8, color='b', ha='right')
            ax3.text(z[i, 0], z[i, 1], z[i, 2], str(i), fontsize=8, color='b', ha='right')

    # Set initial viewing angles
    # Front view
    ax1.view_init(elev=90, azim=-90)
    ax2.view_init(elev=90, azim=-90)
    ax3.view_init(elev=90, azim=-90)

    # # side view
    # ax1.view_init(elev=0, azim=180, roll=-90)
    # ax2.view_init(elev=0, azim=180, roll=-90)
    # ax3.view_init(elev=0, azim=180, roll=-90)

    # # top view
    # ax1.view_init(elev=0, azim=90)
    # ax2.view_init(elev=0, azim=90)
    # ax3.view_init(elev=0, azim=90)

    # Candidate top vertices: [591, 593, 594, 2390, 2391, 2393, 2397, 2398, 2402, 2403]
    # top vertex 2398
    # Candidate bottom vertices: [1023, 1022, 970, 971, 972, 973, 974; 2075, 2020, 2019, 2021, 2022]
    # bottom vertex 2020

    # Labels and titles
    ax1.set_title('Scatter Plot 1')
    ax2.set_title('Scatter Plot 2')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('Y1')
    ax1.set_zlabel('Z1')
    ax2.set_xlabel('X2')
    ax2.set_ylabel('Y2')
    ax2.set_zlabel('Z2')

    pyplot.show()
    return


if __name__ == '__main__':
    print('Program started at ' + datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S %p'))
    start_time = time.time()
    try:
        main()
        run_result = 'Program completed successfully!'
    except Exception as e:
        print(e)
        traceback.print_exc()
        run_result = 'Error: ' + str(e)
    end_time = time.time()
    print('Program ended at ' + datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S %p'))
    print('Execution time: ' + str(datetime.timedelta(seconds=end_time - start_time)))
