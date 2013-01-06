pkgname=mplayer-autocmd-git
pkgver=20130106
pkgrel=1
pkgdesc=""
arch=("any")
url="https://github.com/mineo/mplayer-autocmd"
license=('unknown')
groups=()
depends=('python' 'mplayer')
makedepends=('git')

_gitroot=https://github.com/mineo/mplayer-autocmd.git
_gitname=mplayer-autocmd

build() {
  cd "$srcdir"
  msg "Connecting to GIT server...."

  if [[ -d "$_gitname" ]]; then
    cd "$_gitname" && git pull origin
    msg "The local files are updated."
  else
    git clone "$_gitroot" "$_gitname"
  fi

  msg "GIT checkout done or server timeout"
  msg "Starting build..."

  rm -rf "$srcdir/$_gitname-build"
  git clone "$srcdir/$_gitname" "$srcdir/$_gitname-build"
  cd "$srcdir/$_gitname-build"

}

package() {
  cd "$srcdir/$_gitname-build"
  python setup.py install --root="$pkgdir" --optimize=1
}

# vim:set ts=2 sw=2 et:
