import sys

raise Exception(str(sys.argv))

from lib.commands import (
    import_data,
    print_nl2sql_result,
    top_n_duration_config,
    insert_agent_client,
    keyword_search,
    add_customized_model,
    delete_base_model,
    list_internet_service,
    count_customized_model
)

from lib.database import init_database
from lib.parser import parse_args


def main(args):
    args = parse_args()
    db = init_database()

    match args.function:
        case "import":
            import_data.run(db, args)
        case "topNDurationConfig":
            top_n_duration_config.run(db, args)
        case "insertAgentClient":
            insert_agent_client.run(db, args)
        case "listBaseModelKeyWord":
            keyword_search.run(db, args)
        case "addCustomizedModel":
            add_customized_model.run(db, args)
        case "deleteBaseModel":
            delete_base_model.run(db, args)
        case "listInternetService":
            list_internet_service.run(db, args)
        case "countCustomizedModel":
            count_customized_model.run(db, args)
        case "printNL2SQLresult":
            print_nl2sql_result.run()


if __name__ == "__main__":
    args = parse_args()
    main(args)
