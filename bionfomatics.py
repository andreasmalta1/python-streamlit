import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open("/home/andreas/PycharmProjects/DataVis/dna-logo.jpg")
st.image(image, use_column_width=True)
st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACATGGCAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGAC" \
                 "GTCGCGACTCTGCCCDCATCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCT" \
                 "GAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=125)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header("Input (DNA QUERY)")
sequence
st.header("Output (DNA Nucleotide Count)")
st.subheader("1. Print Dictionary")


def dna_count(seq):
    d = dict([
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("G", seq.count("G")),
        ("C", seq.count("C")),
              ])
    return d


x = dna_count(sequence)
x_label = list(x)
x_values = list(x.values())
x

st.subheader("2. Print text")
st.write("There are " + str(x["A"]) + " adenine (A)")
st.write("There are " + str(x["T"]) + " thymine (T)")
st.write("There are " + str(x["G"]) + " guanine (G)")
st.write("There are " + str(x["C"]) + " cytosine (C)")

st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(x, orient="index")
df
df = df.rename({0: "Count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index": "Nucleotide"})
st.write(df)

st.subheader("4.  Display Bar Chart")
p = alt.Chart(df).mark_bar().encode(
    x="Nucleotide",
    y="Count"
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)
