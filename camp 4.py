#( " what was the largest dinosaur to exist discovered so far?")
#print (" what is the smartest dinosaur discovered so far ")
#print ( " what was the dumbest dinosaur ")
#print (" what was the biggest dinosaur name")
#print ( " What was the first pretador of dinosaurs")
#print ( " what was the last horned dinosaur?")
#print ( " what is the most powerful apex pretador of the creataceous")
# what is the smallest dinosaur
# when did allosaurus live
# where did allosaurus live
# how long was memenchisaurus



#----------------------------------------

questions =[
" what was the heaveist dinosaur discovered so far",
" what is the smartest dinosaur discovered so far",
" what was the longest dinosaur name",
 " what was the pretador of the first dinosaurs",
 " what was the last horned dinosaur ",
 " what was the most powerful apex pretador of all the dinosaurs",
 " what is the smallest dinosaur ",
 " when and where did allosaurus live",
 " how long was memenchisaurus ",
 " what was the largest pterosaur ",
 " what was the most steriotyped dinosaur",
 " what is the order of the period of dinosaurs",
 " did tyrannosaurus rex hunt as a family",
 " what diet did  triceratops and other ceratopsids have in their youth"]

answers=[ " argentinosaurus",
 " troodon",
 " micropachycephalosaurus",
 " archosaurs ",
" triceratops, tryke, tri",
 " mapusaurus ",
 " parvicursor ",
 " creatacous and usa",
 " 110 ft ",
" quetzolquatlus  ",
 " oviraptor ",
 " triassic, jurassic,creatacous ",
 " yes ",
 " omnivore"]

score = 0

for i in range (len(questions)):
    print (questions[i])
    guess = input ("answer:")
    answer=answers[i]
    if guess.lower() in answer.lower():
        print ( " ding ding ding!!!!!")
        score += 1
    else:
        print ( " oof naaah the answer was " + answers [i])
        
    













































