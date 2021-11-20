import sys
import time

def callMe(name, number):
    print("A: Hallo?")
    time.sleep(1)
    print("B: Wie is dat?")
    time.sleep(1)
    print("A: Ik ben het, "+ name)
    time.sleep(1)
    print("B:Hoi "+ name+ " ik ben nu druk kan ik later terug bellen?")
    time.sleep(1)
    print("A: ja hoor.")
    time.sleep(1)
    print("B: wat is je nummer?")
    time.sleep(1)
    print("A: "+number)
    time.sleep(1)
    print("B: oke ik bel je later, doei!")
    time.sleep(1)
    print("A: later!")
    time.sleep(1)
    print("click...")

callMe(sys.argv[1], sys.argv[2])