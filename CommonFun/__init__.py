from flask import make_response, send_from_directory, Response
import shutil


class FileOperator:
    @staticmethod
    def download_file_temp(file_temp_name: str, filename: str) -> Response:
        """
        Download a file in the folder: writable_folder/temp/
        :param file_temp_name: the filename within writable_folder/temp/
        :param filename: the filename in the headers of the response
        :return: A response object
        """
        response = make_response(
            send_from_directory("writable_folder/temp/", file_temp_name.encode('utf-8').decode('utf-8'), as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
        return response

    @staticmethod
    def download_file(file_code: str, filename: str) -> Response:
        """
        Download a file in the folder: writable_folder/file/
        :param file_code: the filename within writable_folder/file_code/
        :param filename: the filename in the headers of the response
        :return: A response object
        """
        response = make_response(
            send_from_directory("writable_folder/file/", file_code.encode('utf-8').decode('utf-8'), as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
        return response

    @staticmethod
    def save_temp_file(temp_file, temp_file_name: str) -> None:
        """
        save a file object into writable_folder/file/
        the temp_file_name should be unique, the following way to set temp_file_name is a good option

        file_seed = str(random.random()) + str(time.time()) + "file_type"
        temp_file_name = hashlib.md5(file_seed.encode("utf-8")).hexdigest()

        :param temp_file: request.files["key"]
        :param temp_file_name: the file name to save in writable_folder/file/
        :return: None
        """
        temp_file.save("writable_folder/temp/" + temp_file_name)

    @staticmethod
    def move_temp_to_file(temp_file: str, file_code: str) -> None:
        """
        The function move a file from writable_folder/temp/ to writable_folder/file/
        :param temp_file: the file name in writable_folder/temp/
        :param file_code: the file name to store in writable_folder/file/
        :return: None
        """
        shutil.copyfile("writable_folder/temp/" + temp_file, "writable_folder/file/" + file_code)
