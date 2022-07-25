import paramiko
import time
import typer

app = typer.Typer()

@app.command()
def hostname(info: str):
    host = "127.0.0.1"
    username = (input("Enter Username: ") or "test")
    password = input("Enter password: ")

    session = paramiko.SSHClient()

    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(hostname=host,
                username=username,
                password=password)

    commands = ['df -k', 'echo $USER', 'hostname']

    for command in commands:
        print(f"{'#'*10} Executing the Command : {command } {'#'*10} ")
        stdin, stdout, stderr = session.exec_command(command)
        time.sleep(.5)
        print(stdout.read().decode())

    session.close()

@app.command()
def goodbye():
    print("Goodbye")

if __name__ == "__main__":
    app()
