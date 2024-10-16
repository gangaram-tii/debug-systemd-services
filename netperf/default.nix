{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.iperf3
    pkgs.python311Full
    pkgs.python311Packages.virtualenv
  ];

  shellHook = ''
    if [ ! -d .venv ]; then
      virtualenv .venv
      source .venv/bin/activate
      pip install paramiko
    else
      source .venv/bin/activate
    fi
    echo "Welcome to your Python development environment."
  '';
}

