# DMOJ problem coci21c2p1, Kaučuk

n = int(input())
section_count = 0
subsection_count = 0
subsubsection_count = 0
section_type_previous = ""

for i in range(n):
	section_input = input().split()
	section_type = section_input[0]
	section_text = section_input[1]

	if section_type == "section":
		section_count = section_count + 1
		print(f"{section_count} {section_text}")
	elif section_type == "subsection":
		subsection_count = subsection_count + 1
		print(f"{section_count}.{subsection_count} {section_text}")
	elif section_type == "subsubsection":
		subsubsection_count = subsubsection_count + 1
		print(f"{section_count}.{subsection_count}.{subsubsection_count} {section_text}")

	if section_type == "section":
		subsection_count = 0
		subsubsection_count = 0
	elif section_type == "subsection":
		subsubsection_count = 0



	

