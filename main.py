import argparse
import taskTrackerFuncs as tt

def main():
    parser = argparse.ArgumentParser(description="A simple Todo list CLI application")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")

    # Subcomando add
    add_parser = subparsers.add_parser("add", help="Adiciona uma nova tarefa")
    add_parser.add_argument("description", type=str, help="Descrição da tarefa")

    # Subcomando update
    update_parser = subparsers.add_parser("update", help="Atualiza uma tarefa existente")
    update_parser.add_argument("id", type=int, help="ID da tarefa a atualizar")
    update_parser.add_argument("NewDescription", type=str, help="Nova descrição da tarefa")

    # Subcomando delete
    delete_parser = subparsers.add_parser("delete", help="Remove uma tarefa")
    delete_parser.add_argument("id", type=int, help="ID da tarefa a remover")

    # Subcomando mark
    mark_parser = subparsers.add_parser("mark", help="Marca uma tarefa como 'A Fazer', 'Fazendo', 'Feito'")
    mark_parser.add_argument("id", type=int, help="ID da tarefa a marcar")
    mark_parser.add_argument("status", type=str, help="Marca a tarefa")

    # Subcomando list
    list_parser = subparsers.add_parser("listar", help="Lista todas as tarefas")
    list_parser.add_argument("--status", type=str, help="Lista tarefas apenas com o status especificado", default="Todas")

    args = parser.parse_args()

    if args.command == "add":
        tt.add_task(args.description)
    elif args.command == "update":
        tt.update_task(args.id, args.NewDescription)
    elif args.command == "delete":
        tt.delete_task(args.id)
    elif args.command == "mark":
        tt.mark_task(args.id, args.status)
    elif args.command == "listar":
        tt.list_tasks(args.status)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()