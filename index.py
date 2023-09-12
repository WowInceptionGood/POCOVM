import pocolib
print(".----.  .----.  .---.  .----. .-. .-..-.   .-.")
print("| {}  }/  {}  \/  ___}/  {}  \| | | ||  `.'  |")
print("| .--' \      /\     }\      /\ \_/ /| |\ /| |")
print("`-'     `----'  `---'  `----'  `---' `-' ` `-'")
print(" ");
print("Welcome to POCOVM menu.");
print("1. Set up DOCKER workspace(if it isnt downloaded")
print("2. Create Linux container")
print("3. Exit")
pick = input()
if (pick == "1"):
	print("What package manager you have?")
	print("1. Apt/Apt-get(Ubuntu Linux/Debian Linux)")
	print("2. PAC (NOT SUPPORTED)")
	pick2 = input()
	if(pick2 == "1"):
		print("Setting up workspace...")
		pocolib.setupworkapt()
		print("Done!")
if (pick == "2"):
	print("What type of distribution you need?")
	print("1. Ubuntu Linux")
	print("2. Debian")
	print("3. RHEL/Fedora")
	pick3 = input()
	if (pick3 == "1"):
		pocolib.cdi(" -it --privileged", " ubuntu", " ")

