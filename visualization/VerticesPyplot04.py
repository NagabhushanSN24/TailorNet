# Plots human w/ garment and garment alone for multiple subjects.

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
    # # female short-pant
    # top_vertex_index, bottom_vertex_index = 2398, 2020  # short-pant female
    # length = numpy.abs(x[top_vertex_index][1] - x[bottom_vertex_index][1])

    # female t-shirt
    top_vertex_index, bottom_vertex_index = 6300, 1299
    length = numpy.linalg.norm(x[top_vertex_index] - x[bottom_vertex_index])

    # print(f'top vertex index: {top_vertex_index}; top_vertex: {x[top_vertex_index]}')
    # print(f'bottom vertex index: {bottom_vertex_index}; bottom_vertex: {x[bottom_vertex_index]}')
    print(f'length: {x[top_vertex_index][1] - x[bottom_vertex_index][1]}')
    return


def main():
    num_rows = 2
    num_cols = 2

    # person_indices = [0, 1, 2, 3, 4, 21, 22, 23, 24]
    person_indices = list(range(25))

    # fig = pyplot.figure()
    axes = []
    scatter_plots = []
    for i_person, person_index in enumerate(person_indices):
        # vertices_body = numpy.load(f'/Users/nagabhushan/SpreeAI/Research/01_SizeBasedTryOn/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0004/model_data/vertices_female_short-pant_{person_index:02}_body_garment.npy')
        vertices_cloth = numpy.load(f'/Users/nagabhushan/SpreeAI/Research/01_SizeBasedTryOn/workspace/clothing_humans/literature/001_TailorNet/runs/testing/test0006/model_data/vertices_female_t-shirt_{person_index:02}_garment.npy')

        find_closest_vertices(vertices_cloth)

    #     ax1 = fig.add_subplot(num_rows, num_cols*2, i_person * 2 + 1, projection='3d')
    #     ax2 = fig.add_subplot(num_rows, num_cols*2, i_person * 2 + 2, projection='3d')
    #     axes.extend([ax1, ax2])
    #
    #     # Plot the scatter plots
    #     x = vertices_body
    #     y = vertices_cloth
    #     scatter1 = ax1.scatter(x[:, 0], x[:, 1], x[:, 2], c='r')
    #     scatter2 = ax2.scatter(y[:, 0], y[:, 1], y[:, 2], c='b')
    #     scatter_plots.extend([scatter1, scatter2])
    #
    #     # Set initial viewing angles
    #     # Front view
    #     ax1.view_init(elev=90, azim=-90)
    #     ax2.view_init(elev=90, azim=-90)
    #
    #     # # side view
    #     # ax1.view_init(elev=0, azim=180, roll=-90)
    #     # ax2.view_init(elev=0, azim=180, roll=-90)
    #
    #     # # top view
    #     # ax1.view_init(elev=0, azim=90)
    #     # ax2.view_init(elev=0, azim=90)
    #
    #     # Labels and titles
    #     ax1.set_title('Scatter Plot 1')
    #     ax2.set_title('Scatter Plot 2')
    #     ax1.set_xlabel('X1')
    #     ax1.set_ylabel('Y1')
    #     ax1.set_zlabel('Z1')
    #     ax2.set_xlabel('X2')
    #     ax2.set_ylabel('Y2')
    #     ax2.set_zlabel('Z2')
    #
    # def on_move(event):
    #     if event.inaxes == axes[0]:
    #         for ax in axes[1:]:
    #             ax.view_init(elev=ax1.elev, azim=ax1.azim, roll=ax1.roll)
    #             fig.canvas.draw_idle()
    #
    # fig.canvas.mpl_connect('motion_notify_event', on_move)
    #
    # pyplot.show()
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
