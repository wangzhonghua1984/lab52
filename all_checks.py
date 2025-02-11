def main():
    checks = [
            (check_reboot, "Pending Reboot."),
            (check_root_full, "Root partition full"),
            ]
everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print("Everything ok.")
   sys.exit(0)
