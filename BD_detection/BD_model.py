import subprocess
import shlex

def run_model(imagepath1, imagepath2):
    # imagepath1 = '/home/peyush/fy_project/xView2/xBD/guatemala-volcano/images/guatemala-volcano_00000000_pre_disaster.png'
    # imagepath2 = '/home/peyush/fy_project/xView2/xBD/guatemala-volcano/images/guatemala-volcano_00000000_post_disaster.png'
    sh_command = []
    # sh_command = shlex.split('/home/peyush/fy_project/xView2/utils/inference.sh  -x /home/peyush/fy_project/xView2 -i '+imagepath1+' -p '+imagepath2+'-l /home/peyush/fy_project/xView2/trained_weights/localization.h5 -c /home/peyush/fy_project/xView2/trained_weights/classification.hdf5 -o /home/peyush/fy_project/xView2/output/result.png -y')
    # sh_command = ['/home/peyush/fy_project/xView2/utils/inference.sh', '-x /home/peyush/fy_project/xView2', '-i '+imagepath1,'-p '+imagepath2, '-l /home/peyush/fy_project/xView2/trained_weights/localization.h5', '-c /home/peyush/fy_project/xView2/trained_weights/classification.hdf5', '-o /home/peyush/fy_project/xView2/output/result.png -y']
    # subprocess.Popen(sh_command)
    subprocess.run(['/home/peyush/fy_project/xView2/utils/inference.sh', '-x', '/home/peyush/fy_project/xView2','-i' , imagepath1, '-p', imagepath2, '-l' ,'/home/peyush/fy_project/xView2/trained_weights/localization.h5', '-c', '/home/peyush/fy_project/xView2/trained_weights/classification.hdf5', '-o',  '/home/peyush/fy_project/xView2/output/result.png', '-y'])
    return True

