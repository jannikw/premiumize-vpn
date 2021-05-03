# Maintainer: Jannik W.
pkgname=premiumize-vpn
pkgver=1.0
pkgrel=1
epoch=
pkgdesc=""
arch=(any)
url=""
license=('MIT')
groups=()
depends=(openvpn)
makedepends=(openvpn)
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=("etc/openvpn/premiumize-auth.txt")
options=()
install=
changelog=
source=()
noextract=()
md5sums=()
validpgpkeys=()

# available vpn locations
VPN_LOCATIONS=("at" "au" "be" "ca" "ch" "cz" "de" "es" "fi" "fr" "gb" "gr" "it" "jp" "nl" "pl" "sg" "us")

build() {
	# adjust vpn configs to read authentication from file
    for loc in "${VPN_LOCATIONS[@]}"
    do
        # cat "$startdir/configs/vpn-$loc.premiumize.me.ovpn" <(echo -e "askpass /etc/openvpn/premiumize-auth.txt\r\n") > "$srcdir/vpn-$loc.premiumize.me.conf"
        sed 's/auth-user-pass/auth-user-pass \/etc\/openvpn\/premiumize-auth.txt/' "$startdir/configs/vpn-$loc.premiumize.me.ovpn" > "$srcdir/vpn-$loc.premiumize.me.conf"
    done
}

package() {
	# create directories with correct permissions
    install -dm750 --owner=openvpn --group=network "$pkgdir/etc/openvpn/client"
    install -dm750 "$pkgdir/etc/sudoers.d"

    # copy files to be installed
    for loc in "${VPN_LOCATIONS[@]}"
    do
        install -m644 --owner=openvpn --group=network "vpn-$loc.premiumize.me.conf" "$pkgdir/etc/openvpn/client/vpn-$loc.premiumize.me.conf"
    done
    install -m600 --owner=openvpn --group=network "$startdir/premiumize-auth.txt" "$pkgdir/etc/openvpn/premiumize-auth.txt"
    install -m600 "$startdir/90-vpn-premiumize" "$pkgdir/etc/sudoers.d/90-vpn-premiumize"
    install -Dm755 "$startdir/vpn-premiumize-block.py" "$pkgdir/opt/vpn-premiumize/vpn-premiumize-block.py"
}
