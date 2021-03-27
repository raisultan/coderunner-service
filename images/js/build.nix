let
  pkgs =
    import ../common/nixpkgs.nix;

  build_image =
    import ../common/build_image.nix;

  imgNodeModules =
    import ./img_node_modules/default.nix { pkgs = pkgs; };
in
build_image {
  pkgs = pkgs;
  name = "raisultan/js";
  tag = "latest";
  installedPackages = [
    pkgs.nodejs
  ];
  env = [
    "PATH=${pkgs.nodejs}/bin/:${imgNodeModules}/libexec/img_node_modules/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    "NODE_PATH=${imgNodeModules}/libexec/img_node_modules/node_modules"
  ];
}
