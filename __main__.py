import argparse
import zoom_joiner.test.initialise as initialise
import zoom_joiner.test.addTimetable as timetable

def main():
    parser = argparse.ArgumentParser(description="Display all the lessons")
    parser.add_argument("-i","--initialise", dest="initialise")
    args = parser.parse_args()

    if args.initialise:
        if str(args.initialise)=="lesson":
            initialise.Initialise()
        elif str(args.initialise)=="timetable":
            timetable.SetTimetable()            

if __name__ == "__main__":
    main()
