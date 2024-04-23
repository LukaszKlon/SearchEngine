import wikipedia
import os
import threading
wikipedia.set_lang("simple")

Path = os.path.abspath("YourPath\\WikipediaArticles")
s = set()


def wikipedia_crawler(start_topic, depth=5):
    visited_topics = set()
    topics_to_visit = [(start_topic, depth)]

    while topics_to_visit:
        current_topic, current_depth = topics_to_visit.pop(0)
        print(current_depth)
        try:
            if current_depth <= 0:
                continue
            
            if current_topic in visited_topics:
                continue
            
            
            page = wikipedia.page(current_topic)
        
            
            filepath = os.path.join(Path,current_topic+".txt")
            if page.content in s:
                print("Same")
                continue
            s.add(page.content)
            print(current_topic)
            file = open(filepath,'w',encoding='utf-8')
            file.write(page.content)
            file.close()

            
            visited_topics.add(current_topic)
            
            links = page.links
            for link in links:    
                topics_to_visit.append((link, current_depth - 1))
        except Exception as e:
            continue


topics_and_depths = [("Rome", 4), ("Lisbon", 4), ("Paris", 4),("Yugoslavia",4),
                     ("Iga_Świątek", 4), ("Novak_Djokovic", 4), ("Rafael_Nadal", 4),("Roger_Federer",4),
                     ("World_War_II", 4), ("Adolf Hitler", 4), ("Lionel Messi", 4),("Cristiano_Ronaldo",4),
                     ("FC_Bayern_Munich", 4), ("Mount_Everest", 4), ("Australia", 4),("Star_Wars",4),
                     ("Harry_Potter", 4), ("James_Cameron", 4), ("United_States", 4),("The_Lord_of_the_Rings",4),
                     ("Anfield", 4), ("Johan_Cruyff", 4), ("Werner_Heisenberg", 4),("Erwin_Schrödinger",4),
                     ("Olympic_Games", 4), ("Facebook", 4), ("Jagiellonian_University", 4),("Conor_McGregor",4),
                     ("Audi", 4), ("Toyota", 4), ("Lamborghini", 4),("FA_Cup",4),
                     ("Manchester_United_F.C.", 4), ("Premier_League", 4), ("Serie_A", 4),("La_Liga",4),
                     ("Bundesliga", 4), ("Juventus_F.C.", 4), ("Canyon", 4),("Heroin",4),
                     ("Copa_América", 4), ("Kardashian", 4), ("Nelson_Mandela", 4),("LGBT",4),
                     ("Volleyball", 4), ("The_Rolling_Stones", 4), ("Coldplay", 4),("Pink_Floyd",4),
                     ("Nirvana", 4), ("The_Beatles", 4), ("Queen", 4),("Metallica",4),
                     ("Guns_N%27_Roses", 4), ("Eddy_Merckx", 4), ("Titanic", 4),("Cannabis_(drug)",4)]


threads = []
for topic, depth in topics_and_depths:
    thread = threading.Thread(target=wikipedia_crawler, args=(topic, depth))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

