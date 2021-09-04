from document_classification import NaiveBayes
from decision_tree_learning import build_tree,classify
sentences = [
    ('real', 'yes if i do n\'t have anything plan for the day'),
    ('generated', 'if i do n\'t have n\'t plan for the day'),
    ('real', 'i would like to remind you that music is very important'),
    ('generated', 'i would like to jack you that music is very'),
    ('real', 'it would be unfair for me to ask you to wait'),
    ('generated', 'it would be earlier for me to ask you to'),
    ('real', 'i am answering this so you can vote'),
    ('generated', 'i am doing this so you can vote '),
    ('real', 'well in my case it is because i watch and excessive amount of television'),
    ('generated', 'if it is because i watch and excessive amount of'),
    ('real', 'rich people tend to think they are better than everyone else'),
    ('generated', 'allow tend to think they are better than than '),
    ('real', 'i tried your email it did n\'t work i put it on here instead'),
    ('generated', 'it did n\'t work i put it on here '),
    ('real', 'without any more information it would be difficult to go any further than that'),
    ('generated', 'it would be difficult to go any further than '),
    ('real', 'there are many reasons that are no good for a person that gets hurt'),
    ('generated', 'that are no good for a person that gets '),
    ('real',
     'i usually go here to get my tim horton s fix since i work right by it it is a typical mall has a few useful stores is one wish i could say more but it is what it is'),
    ('generated', 'i usually go here to get my tim horton father father'),
    ('real', 'c\'mon who does n\'t love this great beer selection and cool outside beer tent on a warm september day'),
    ('generated', 'c\'mon who does n\'t love this great beer selection themed themed'),
    ('real', 'maybe i just did n\'t get the right food here..'),
    ('generated', 'maybe i just did n\'t get the right food fight fight'),
    ('real', 'i\'m biased because i received my and will receive my from cmu however i\'m very happy'),
    ('generated', 'i\'m biased because i received my and sonny except except'),
    ('real', 'fast food style mexican food chain it was just ok'),
    ('generated', 'fast food style mexican food chain it was just amazing amazing'),
    ('real',
     'great customer service excellent coffee relaxing atmosphere free wifi its close to home and i enjoy coming here in the mornings'),
    ('generated', 'great customer service excellent coffee trail atmosphere free wifi mekong mekong'),
    ('real', 'the service is terrible we cancelled our contract after 5-6 notifications and warnings'),
    ('generated', 'do n\'t waste your time and money the service go go'),
    ('real', 'their food is pretty good this is a great stop when nothing is cooked at home'),
    ('generated', 'great take out place they have a huge selection'),
    ('real', 'i live 12 miles away and try to find reasons to meet people here'),
    ('generated', ' 12 miles away and try to find part'),
    ('real', 'it has all the great flavors i like and an awesome drink menu'),
    ('generated', 'great food and drinks i just love this place'),
    ('real', 'the mac cheese and the sweet potato fries are all good'),
    ('generated', 'i really enjoy this restaurant the sandwiches the salads'),
    ('real', 'whatever you do do not act desperate'),
    ('generated', 'whatever you do do not act like that'),
    ('real', 'yahoo music is free and it rocks'),
    ('generated', 'yahoo music is free and free music'),
    ('real', 'however it is a good magazine'),
    ('generated', 'i love that show'),
    ('real', 'it will not work like that'),
    ('generated', 'i love taylor but i do not like him'),
    ('real', 'i believe you know the answer to this question miss'),
    ('generated', 'i think you should tell her what is going'),
    ('real', 'there is nothing wrong with you'),
    ('generated', 'do not be afraid to say that you are'),
    ('real', 'i can not wait for the answer'),
    ('generated', 'i can not wait for the answer to this question question'),
    ('real', 'i have never heard of it and i am using reverse on you'),
    ('generated', 'i think it is funny '),
    ('real', 'did you see what your monkey just did'),
    ('generated', 'did you see what your mother was in '),
    ('real', 'let me know if that helps'),
    ('generated', 'his birthday is on a monkey '),
    ('real', 'he a type well that\'s what it looked like in the photos'),
    ('generated', 'i agree that\'s what it looked like in the'),
    ('real', 'i bought this today and i absolutely love it'),
    ('generated', 'i bought this today and i love love jane it'),
    ('real', 'it\'s not really located in the best area'),
    ('generated', 'the process here was super an they sat us something something'),
    ('real', 'food is so good i\'ll be back for sure healthy or happy meal either way'),
    ('generated', 'decent place for a quickie an do n\'t go feels feels'),
    ('real', 'i\'ve been waiting for this location to open for a while'),
    ('generated', 'the food is over priced for the size of great great'),
    ('real', 'i\'m not much of a coffee drinker but on a hot day maybe after going to the farmer\'s market'),
    ('generated', 'i actually enjoyed this place the food was great but but'),
    ('real', 'i\'ve been bringing my car here for its oil changes for several years'),
    ('generated', 'the only reason why i gave it 3 stars go go'),
    ('real', 'this is where i shop on black friday when everything is 50 off'),
    ('generated', 'i had my birthday dinner here and everything was lunch lunch'),
    ('real', 'i apologize but are you okay in there are you just typing crap'),
    ('generated', 'are you okay in there are you just all'),
    ('real', 'have to update my review today have been here a few other times and always had excellent food'),
    ('generated', 'this is a must visit the place is small pizzeria pizzeria'),
    ('real', 'some women may think so but there are always others that do not'),
    ('generated', 'i think so but there are always others that'),
    ('real', 'when i received my first mail from ... ...'),
    ('generated', 'sir what you said meant search nothing somebody ..'),
    ('real', 'super delicious ... everything that i\'ve ever had there has been delicious')
]

if __name__ == '__main__':
    percent = int(input())
    sentence = input()
    cetirieset=len(sentences)*0.4
    train_set=sentences[:cetirieset]
    test_set=sentences[cetirieset:]

    klasifikator_first=NaiveBayes(train_set)
    klasifikator_second=NaiveBayes(train_set)

    tree = build_tree(train_set)
    klasifikacija_drvo = classify(sentence, tree)

    for data in train_set:
     klasifikator_first.train(data[0],data[1])
     klasifikator_second.train(data[0],data[1])


     klasifikator_first.classify_document(sentence)
     klasifikator_second.classify_document(sentence)

    print(f"Klasa dobiena so naiven baesov klasifikator:{}")
    print(f"Klasa dobiena so drvo na odluka:{klasifikacija_drvo}")


