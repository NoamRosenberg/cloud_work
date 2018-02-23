import sys
import argparse
parser = argparse.ArgumentParser()
from old_school_model import Graph


parser.add_argument('--model_type', type=str, default='regular',
help='regular or layer model')

parser.add_argument('--epochs', type=int, default=20)

parser.add_argument('--batch_size', type=int, default=128)


		
def main():

	graph = Graph(FLAGS)
	graph.run()


if __name__ == '__main__':
	FLAGS, unparsed = parser.parse_known_args()
	main()

