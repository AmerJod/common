from cadetlib.sourcecode.repository_type import *  #### DON'T DELETE THIS LINE ####

from cadetlib.logging import logger


class SourceCodeFactory(object):
    """
        SourceFactory Factory
    """

    sourcecode_dict = {}

    @staticmethod
    def create(source_code_type, uri, credentials, branch):
        """
            Jsonify object depends on the class name
        Args:
            source_code_type (string): source code type
            uri (string): url of the repository
            credentials (dict): could be token || username&password
            branch (string): branch name, default value: master
        Return:
            source_code object
        """

        if source_code_type is not SourceCodeFactory.sourcecode_dict:
            try:
                # add it to the ChartFactory list
                SourceCodeFactory.sourcecode_dict[source_code_type] = eval(
                    source_code_type + ".Factory()"
                )

            except:

                logger.debug(f"model: ChartFactory, {source_code_type},  Not found")
                return None

        logger.debug(f"model: Source code created instance of {source_code_type}")
        sourcecode_repo_class = SourceCodeFactory.sourcecode_dict[source_code_type]
        sourcecode_repo_object = sourcecode_repo_class.create(uri=uri, credentials=credentials, branch=branch)

        return sourcecode_repo_object



# TODO: for testing- delete later-  Amer OR moved to a testing
if __name__ == "__main__":

    # sourcecode_list = ["AzureDev"]
    # uri = "dev.azure.com/BTL-SecOps/Cadet%20Core/_git/Cadet%20Core"
    # credentials = {"token": "zwif32d6xwqheffjcfkj6bzxzog7bvjry2m2eypaljsicwwie6ma"}

    sourcecode_list = ["AzureDev"]
    uri = "dev.azure.com/BTL-SecOps/Cadet%20Core/_git/Cadet%20Core"
    credentials = {"token": "kgubxdu6lyfha3h35whpemkdbksgs3unkzoncxgmh6tdzf5cl35q"}

    for source_code in sourcecode_list:
        repo = SourceCodeFactory.create(source_code_type=source_code, uri=uri, credentials=credentials, branch='dev')
        if source_code == "AzureDev":
            print(repo.download("Token",'/'))
        else:
            repo.download('')
