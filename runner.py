# runner.py
import os

from kanbanf.app import create_app

instance = os.environ['KANBANF_INST']

print(f"Kanbanf app instanced in '{instance}' environment")

app = create_app(instance)

if __name__ == '__main__':
    app.run()
