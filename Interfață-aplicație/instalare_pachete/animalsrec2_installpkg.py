from naoqi import ALProxy


def install_package(robot_ip, package_path):
    try:
        pm_proxy = ALProxy("PackageManager", robot_ip, 9559)
        pm_proxy.install(package_path) # Instalare pachet
    except Exception as e:
        print(e)


if __name__ == "__main__":
    robot_ip = "192.168.1.100"
    package_path = "/home/nao/packages/animalsrecognitionn2-4053d0-0.0.1.pkg"

    install_package(robot_ip, package_path)
