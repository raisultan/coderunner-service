{ pkgs }:

let
  codeRunnerSrc =
    builtins.fetchGit {
      url = "https://github.com/glotcode/code-runner";
      ref = "refs/heads/main";
      rev = "c6faaf9c7a7715ea7bfc4603383a04a41679a01b";
    };

  codeRunner =
    import "${codeRunnerSrc}/Cargo.nix" { pkgs = pkgs; };
in
codeRunner.rootCrate.build
