#!/usr/bin/python
"""Get AWS CLI environment variables."""

import argparse

block = "[jenkinsdemo]"
configs = {'AWS_ACCESS_KEY_ID': '', 'AWS_SECRET_ACCESS_KEY': ''}


def Get_credentials(profile, credential, in_file):
    """Get credentials."""
    for line in in_file:
        if line.strip() == block:
            break
        if line.find(credential) > -1:
            strResult = line[line.find("=")+1:] if line.find('=') > -1 else None
            return strResult.strip()


def main():
    """Get entry-point."""
    with open('/opt/.aws/credentials', "r") as in_file:
        configs['AWS_ACCESS_KEY_ID'] = Get_credentials(block, 'aws_access_key_id', in_file=in_file)
        configs['AWS_SECRET_ACCESS_KEY'] = Get_credentials(block, 'aws_secret_access_key', in_file=in_file)
        parser = argparse.ArgumentParser(__file__, __doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument("--variable", help="AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY")
        args = parser.parse_args()

        if not args.variable:
            parser.exit(status=1, message="Missing --variable Must choose between \
        AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY \n")

        if args.variable == "AWS_SECRET_ACCESS_KEY":
            print('export {key}="{value}"'.format(key="AWS_SECRET_ACCESS_KEY", value=configs['AWS_SECRET_ACCESS_KEY']))

        if args.variable == "AWS_ACCESS_KEY_ID":
            print('export {key}="{value}"'.format(key="AWS_ACCESS_KEY_ID", value=configs['AWS_ACCESS_KEY_ID']))


if __name__ == '__main__':
    main()
