import boto3
from datetime import datetime
import os


def write_file_s3():

    try:

        session = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
    
        file_name = "test_file_{dttime}.txt".format(dttime=datetime.now().strftime('%m%d%Y'))

        write_string = "This is a test string written on {dttime}".format(dttime=datetime.now().strftime('%m%d%Y_%H%M%S'))

        s3 = session.resource('s3')

        path = "bi-dev-2022"
        s3_path = ""
        s3_path += file_name

        object = s3.Object(path, s3_path)
        object.put(Body=write_string)

    except:
        raise(Exception)


if __name__ == "__main__":
    write_file_s3()