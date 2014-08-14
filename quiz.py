questions = [{'question':'Capital of India','answer':'new delhi'},{'question':'Capital of Italy','answer':'rome'},{'question':'Capital of Ireland','answer':'dublin'}]
score = 0

for q in questions:
	answer = raw_input(q['question']+' :')
	if answer == q['answer']:
		score = score + 1
		print "right answer, kudos"
	else:
		print "wrong score"

print "Final score is", score