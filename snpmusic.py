#!/usr/bin/env python3
import sys
from Bio import SeqIO
from mingus.containers import Composition, Track
from mingus.containers import MidiInstrument
from mingus.midi import midi_file_out as MidiFileOut


base_to_note_mapping = {
  'A': 'C',
  'G': 'E',
  'C': 'G',
  'T': 'B'
}

a_genotype = {'X': {}, 'Y': {}}
b_genotype = {'X': {}}
ref_genotype = {'X': {}, 'Y': {}}

ref_instrument = MidiInstrument('Acoustic Grand Piano')
a_instrument = MidiInstrument('Shakuhachi')
b_instrument = MidiInstrument('Electric Guitar')


ref_track = Track(ref_instrument)
a_track = Track(a_instrument)
b_track = Track(b_instrument)


for i in range(1,23):
    a_genotype[str(i)]={}
    b_genotype[str(i)]={}
    ref_genotype[str(i)]={}

print('reading SNP data')
with open(sys.argv[1], 'r') as file:
  for line in file:
    if not line.startswith('#'):
      [rsid, chromosome, pos, genotype] = line.rstrip().split('\t')
      if not chromosome == 'MT':
        a_genotype[str(chromosome)][pos] = genotype[0]
        if not chromosome == 'Y' and len(genotype) == 2:
          b_genotype[str(chromosome)][pos] = genotype[1]

print('reading reference human genome')
for chromosome in a_genotype:
  filename = 'chr'+chromosome+'.fa'
  seq_record_count = 1
  for seq_record in SeqIO.parse(filename,'fasta'):
    #print(seq_record_count)
    seq_record_count = seq_record_count+1
    for pos in a_genotype[chromosome]:
      ref_genotype[chromosome][pos] = seq_record[int(pos)-1]

print('turning into music')
limit = 1024
count = 0
for chromosome in a_genotype:
  if count > limit:
    break
  for pos in a_genotype[chromosome]:
    try:
      if count > limit:
        break
      if a_genotype[chromosome][pos] in base_to_note_mapping and a_genotype[chromosome][pos] in base_to_note_mapping:
        ref_track + base_to_note_mapping[ref_genotype[chromosome][pos]]
        a_track + base_to_note_mapping[a_genotype[chromosome][pos]]
        b_track + base_to_note_mapping[b_genotype[chromosome][pos]]
        count = count + 1
        #print(pos,ref_genotype[chromosome][pos],a_genotype[chromosome][pos],b_genotype[chromosome][pos])
    except KeyError:
        f = ''

print('writing out midi file')
c = Composition()

c.set_author('Matthew Berryman', 'matthew@acrossthecloud.net')
c.set_title('Matthew Berryman')

c.add_track(ref_track)
c.add_track(a_track)
c.add_track(b_track)

MidiFileOut.write_Composition('matthew_berryman.mid',c)