class Noob < Formula
  include Language::Python::Virtualenv

  desc "Generate Homebrew formulae for npm packages"
  homepage "https://github.com/zmwangx/homebrew-npm-noob"
  url "https://github.com/zmwangx/homebrew-npm-noob/archive/v0.1.tar.gz"
  sha256 "e78a85db1778729e5f4ecac038be09cc62c0236f589c242dfaefd11487cede86"

  depends_on :python3

  def install
    virtualenv_create(libexec, "python3")
    system libexec/"bin/pip", "install", "."
    bin.install_symlink libexec/"bin/noob"
    man1.install "manpages/noob.1"
  end

  test do
    assert_match "class Svgo < Formula", shell_output("#{bin}/noob svgo")
  end
end
