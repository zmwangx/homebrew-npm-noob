class Noob < Formula
  include Language::Python::Virtualenv

  desc "Generate Homebrew formulae for npm packages"
  homepage "https://github.com/zmwangx/homebrew-npm-noob"
  url "https://github.com/zmwangx/homebrew-npm-noob/archive/v0.2.tar.gz"
  sha256 "15e2ac4cbf3e549f62199e3b0e3c8d5fbc94043a7aba1b04786f37dffc41de11"

  depends_on "python3"

  def install
    virtualenv_create(libexec, "python3")
    system libexec/"bin/pip", "install", "."
    bin.install_symlink libexec/"bin/noob"
    man1.install "docs/noob.1"
  end

  test do
    assert_match "class Svgo < Formula", shell_output("#{bin}/noob svgo")
  end
end
