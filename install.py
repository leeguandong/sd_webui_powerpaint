import launch

if not launch.is_installed("mmagic"):
    try:
        launch.run_pip("install mmagic", "requirements for mmagic")
    except Exception:
        print("Can't install mmagic. Please follow the readme to install manually")

if not launch.is_installed("mmengine"):
    try:
        launch.run_pip("install mmengine==0.8.5", "requirements for mmengine")
    except Exception:
        print("Can't install mmengine. Please follow the readme to install manually")

if not launch.is_installed("controlnet-aux"):
    try:
        launch.run_pip("install controlnet-aux==0.03", "requirements for controlnet-aux")
    except Exception:
        print("Can't install controlnet-aux. Please follow the readme to install manually")
