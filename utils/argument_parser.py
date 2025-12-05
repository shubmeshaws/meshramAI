```python
import argparse

def parse_args(description, args_list):
    """
    Parse command-line arguments.

    Args:
        description (str): Description of the script.
        args_list (list): List of tuples containing argument information.
            Each tuple should have the following format:
            (arg_name, arg_type, arg_help, required)

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description=description)

    for arg in args_list:
        if len(arg) == 4:
            arg_name, arg_type, arg_help, required = arg
            if required:
                parser.add_argument(f"--{arg_name}", type=arg_type, help=arg_help, required=True)
            else:
                parser.add_argument(f"--{arg_name}", type=arg_type, help=arg_help)
        else:
            raise ValueError("Invalid argument format. Expected (arg_name, arg_type, arg_help, required).")

    return parser.parse_args()


def main():
    # Example usage
    args_list = [
        ("region", str, "AWS region", True),
        ("bucket_name", str, "S3 bucket name", False)
    ]

    description = "AWS S3 utility script"
    args = parse_args(description, args_list)

    print(f"Region: {args.region}")
    print(f"Bucket Name: {getattr(args, 'bucket_name', None)}")


if __name__ == "__main__":
    main()
```
