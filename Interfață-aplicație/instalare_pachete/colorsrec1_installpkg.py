from naoqi import ALProxy


def install_package(robot_ip, package_path):
    try:
        pm_proxy = ALProxy("PackageManager", robot_ip, 9559)
        pm_proxy.install(package_path)  # Instalare pachet
    except Exception as e:
        print(e)


if __name__ == "__main__":
    robot_ip = "192.168.1.100"
    package_path = "/home/nao/packages/colorrecognition1-416eaf-0.0.2.pkg"

    install_package(robot_ip, package_path)
