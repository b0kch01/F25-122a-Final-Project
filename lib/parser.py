import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="project.py", description="122a Final Project CLI for Agent Platform"
    )

    function_subparser = parser.add_subparsers(
        title="function", dest="function", required=True
    )

    # IMPORT
    import_parser = function_subparser.add_parser(
        "import", help="Imports data in a given directory. Deletes existing tables."
    )
    import_parser.add_argument("folderName", type=str)

    # INSERT AGENT
    insert_agent_parser = function_subparser.add_parser(
        "insertAgentClient", help="Insert a new agent client into the related tables."
    )
    insert_agent_parser.add_argument("uid", type=int)
    insert_agent_parser.add_argument("username", type=str)
    insert_agent_parser.add_argument("email", type=str)
    insert_agent_parser.add_argument("card_number", type=int)
    insert_agent_parser.add_argument("card_holder", type=str)
    insert_agent_parser.add_argument("expiration_date", type=str)
    insert_agent_parser.add_argument("cvv", type=int)
    insert_agent_parser.add_argument("zip", type=int)
    insert_agent_parser.add_argument("interests", type=str)

    # ADD CUSTOMIZED MODEL
    add_customized_model_parser = function_subparser.add_parser(
        "addCustomizedModel", help="Add a new customized model to the tables."
    )
    add_customized_model_parser.add_argument("mid", type=int)
    add_customized_model_parser.add_argument("bmid", type=int)

    # DELETE BASE MODEL
    delete_base_model_parser = function_subparser.add_parser(
        "deleteBaseModel", help="Delete a base model from the tables."
    )
    delete_base_model_parser.add_argument("bmid", type=int)

    # LIST INTERNET SERVICES
    list_internet_services_parser = function_subparser.add_parser(
        "listInternetService",
        help="Given a base model id, lists all the internet services that the model is utilizing, sorted by provider’s name in ascending order.",
    )
    list_internet_services_parser.add_argument("bmid", type=int)

    # COUNT CUSTOMIZED MODEL

    # FIND TOP-N LONGEST DURATION CONFIGURATION
    top_n_duration_parser = function_subparser.add_parser(
        "topNDurationConfig",
        help="Given an agent client id, list the top-N longest duration configurations with the longest duration managed by that client. Sorted in descending order.",
    )
    top_n_duration_parser.add_argument("uid", type=int)
    top_n_duration_parser.add_argument("N", type=int)

    # KEYWORD SEARCH
    keyword_search_parser = function_subparser.add_parser(
        "listBaseModelKeyWord",
        help="List 5 base models that are utilizing LLM services whose domain contains the keyword, sorted by bmid in ascending order.",
    )
    keyword_search_parser.add_argument("keyword", type=str)

    # PRINT Q9 RESULTS
    nl2q_parser = function_subparser.add_parser(
        "printNL2SQLresult", help="Prints q9.csv table"
    )

    return parser.parse_args()
