from livereload import Server, shell

if __name__ == "__main__":
    command = "make html"

    server = Server()
    server.watch("docs/source/**/*.rst", shell(command, cwd="docs"), delay=1)
    server.watch("docs/source/**/*.md", shell(command, cwd="docs"), delay=1)
    server.watch("docs/source/**/*.py", shell(command, cwd="docs"), delay=1)
    server.watch("docs/source/**/*.csv", shell(command, cwd="docs"), delay=1)
    server.watch("docs/source/_static/*", shell(command, cwd="docs"), delay=1)
    server.watch("docs/source/_templates/*", shell(command, cwd="docs"), delay=1)
    server.watch("boilerplate_python/**/*.py", shell(command, cwd="docs"), delay=1)
    server.watch("README.md", shell(command, cwd="docs"), delay=1)
    server.serve(root="docs/build/html", host="0.0.0.0", port=5500)
