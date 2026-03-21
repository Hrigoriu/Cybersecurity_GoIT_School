import argparse
from database.db import get_db_session
from database.models import Teacher, Group, Student, Subject
from repositories.base import BaseRepository
from utils.logger import RetroLogger

MODELS_MAP = {
    "Teacher": Teacher,
    "Group": Group,
    "Student": Student,
    "Subject": Subject,
}


def main():
    """
    Головний контролер застосунку (CLI інтерфейс).
    Обробляє аргументи командного рядка та викликає відповідний репозиторій.
    """
    parser = argparse.ArgumentParser(
        description="Terminal Interface for Database Records"
    )
    parser.add_argument(
        "-a", "--action", choices=["create", "list", "update", "remove"], required=True
    )
    parser.add_argument("-m", "--model", choices=MODELS_MAP.keys(), required=True)
    parser.add_argument("-i", "--id", type=int)
    parser.add_argument("-n", "--name", type=str)

    args = parser.parse_args()
    model_class = MODELS_MAP[args.model]

    with get_db_session() as session:
        repo = BaseRepository(session, model_class)
        RetroLogger.info(
            f"Виконання операції {args.action.upper()} для сутності {args.model}..."
        )

        if args.action == "create":
            if not args.name:
                RetroLogger.error("Пропущено аргумент --name")
                return

            kwargs = {
                "fullname" if hasattr(model_class, "fullname") else "name": args.name
            }
            if args.model == "Student":
                kwargs["group_id"] = 1
            elif args.model == "Subject":
                kwargs["teacher_id"] = 1

            record = repo.create(**kwargs)
            RetroLogger.data(f"Створено запис: ID {record.id}")

        elif args.action == "list":
            records = repo.get_all()
            for rec in records:
                val = rec.fullname if hasattr(rec, "fullname") else rec.name
                RetroLogger.data(f"[{rec.id}] : {val}")

        elif args.action == "update":
            if not args.id or not args.name:
                RetroLogger.error("Потрібні аргументи --id та --name")
                return
            kwargs = {
                "fullname" if hasattr(model_class, "fullname") else "name": args.name
            }
            if repo.update(args.id, **kwargs):
                RetroLogger.data(f"Оновлено запис ID {args.id}")

        elif args.action == "remove":
            if not args.id:
                RetroLogger.error("Пропущено аргумент --id")
                return
            if repo.delete(args.id):
                RetroLogger.warn(f"Запис ID {args.id} видалено назавжди.")


if __name__ == "__main__":
    main()
