import sys
from elftools.elf.elffile import ELFFile
from elftools.common.exceptions import ELFError
from elftools.elf.segments import NoteSegment

class ReadELF(object):

    def __init__(self, file):
        self.elffile = ELFFile(file)

    def get_build(self):
        for segment in self.elffile.iter_segments():
            if isinstance(segment, NoteSegment):
                for note in segment.iter_notes():
                    print note

def main():
    if(len(sys.argv) < 2):
        print "Missing argument"
        sys.exit(1)

    with open(sys.argv[1], 'rb') as file:
        try:
            readelf = ReadELF(file)
            readelf.get_build()

        except ELFError as err:
            sys.stderr.write('ELF error: %s\n' % err)
            sys.exit(1)

if __name__ == '__main__':
    main()
