import argparse

def main():
    
    parser = argparse.ArgumentParser(description="program to detect SSN presence in files")
    parser.add_argument('--confidence', type=float, default=0.5, help="required confidence from the sampling algorithm (default value of 0.5)")
    parser.add_argument('--margin-error', type=float, default=0.05, help="required margin of error from the sampling algorithm (default value of 0.05)")
    args = parser.parse_args() 

    print("hello World ", args.location, args.confidence)

if __name__ == "__main__":
    main()
