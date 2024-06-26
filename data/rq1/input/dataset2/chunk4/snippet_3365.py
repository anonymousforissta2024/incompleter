#Source: https://stackoverflow.com/questions/65431109/matplotlib-xlim-typeerror-not-supported-between-instances-of-int-and-lis
import os
import matplotlib.pyplot as plt
import argparse
from attacker import check_attack_type

IMG_DIR = "./plots"

def read_lines(f, d):
    lines = f.readlines()[:-1]
    for line in lines:
        typ, time, num = line.split(',')
        if typ == 'seq':
            d['seq']['time'].append(float(time))
            d['seq']['num'].append(float(num))
        elif typ == 'ack':
            d['ack']['time'].append(float(time))
            d['ack']['num'].append(float(num))
        else:
            raise "Unknown type read while parsing log file: %s" % typ

def main():
    parser = argparse.ArgumentParser(description="Plot script for plotting sequence numbers.")
    parser.add_argument('--save', dest='save_imgs', action='store_true',
                        help="Set this to true to save images under specified output directory.")
    parser.add_argument('--attack', dest='attack',
                        nargs='?', const="", type=check_attack_type,
                        help="Attack name (used in plot names).")
    parser.add_argument('--output', dest='output_dir', default=IMG_DIR,
                        help="Directory to store plots.")
    args = parser.parse_args()
    save_imgs = args.save_imgs
    output_dir = args.output_dir
    attack_name = args.attack

    if save_imgs and attack_name not in ['div', 'dup', 'opt'] :
        print("Attack name needed for saving plot figures.")
        return

    normal_log = {'seq':{'time':[], 'num':[]}, 'ack':{'time':[], 'num':[]}}
    attack_log = {'seq':{'time':[], 'num':[]}, 'ack':{'time':[], 'num':[]}}
    normal_f = open('log.txt', 'r')
    attack_f = open('%s_attack_log.txt' % attack_name, 'r')
    
    read_lines(normal_f, normal_log)
    read_lines(attack_f, attack_log)
   
    if attack_name == 'div':
        attack_desc = 'ACK Division'
    elif attack_name == 'dup':
        attack_desc = 'DupACK Spoofing'
    elif attack_name == 'opt':
        attack_desc = 'Optimistic ACKing'
    else:
        raise 'Unknown attack type: %s' % attack_name
    norm_seq_time, norm_seq_num = normal_log['seq']['time'], normal_log['seq']['num']
    norm_ack_time, norm_ack_num = normal_log['ack']['time'], normal_log['ack']['num']
    atck_seq_time, atck_seq_num = attack_log['seq']['time'], attack_log['seq']['num']
    atck_ack_time, atck_ack_num = attack_log['ack']['time'], attack_log['ack']['num']
    plt.plot(norm_seq_time, norm_seq_num, 'b^', label='Regular TCP Data Segments')
    plt.plot(norm_ack_time, norm_ack_num, 'bx', label='Regular TCP ACKs')
    plt.plot(atck_seq_time, atck_seq_num, 'rs', label='%s Attack Data Segments' % attack_desc)
    plt.plot(atck_ack_time, atck_ack_num, 'r+', label='%s Attack ACKs' % attack_desc)
    plt.legend(loc='upper left')

    x = max(max(norm_seq_time, norm_ack_time),max(atck_seq_time, atck_ack_time))
    y = max(max(norm_seq_num, norm_ack_num),max(atck_seq_num, atck_ack_num))
    plt.xlim(0, x)
    plt.ylim(0,y)

    plt.xlabel('Time (s)')
    plt.ylabel('Sequence Number (Bytes)')

    if save_imgs:
        # Save images to figure/
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        plt.savefig(output_dir + "/" + attack_name)
    else:
        plt.show()
    
    normal_f.close()
    attack_f.close()


if __name__ == "__main__":
    main()