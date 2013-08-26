pkgname=mplayer-autocmd-git
pkgver=3.2.g955cec3
pkgrel=1
pkgdesc=""
arch=("any")
url="https://github.com/mineo/mplayer-autocmd"
license=('unknown')
source=('git+https://github.com/mineo/mplayer-autocmd.git')
md5sums=('SKIP')
depends=('python' 'mplayer')
makedepends=('git')

pkgver(){
  cd "${srcdir}/mplayer-autocmd"
  echo "$(git describe --tags --always | sed 's/-/./g' )"
}

package() {
  cd "${srcdir}/mplayer-autocmd"
  python setup.py install --root="$pkgdir" --optimize=1
}

# vim:set ts=2 sw=2 et:
