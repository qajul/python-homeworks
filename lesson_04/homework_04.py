adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())

print(adwentures_of_tom_sawer)

# task 04
print(adwentures_of_tom_sawer.count("h"))

# task 05
words = adwentures_of_tom_sawer.split()
capital_words = 0

for word in words:
    if word[0].isupper():
        capital_words += 1

print(capital_words)

# task 06
first_name_tom = adwentures_of_tom_sawer.find("Tom")
second_name_tom = adwentures_of_tom_sawer.find("Tom", first_name_tom + 1)

print(second_name_tom)

# task 07
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")

# task 08
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print("Речення яке почмнається з By the time є")

# task 10
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words = last_sentence.split()

print(len(words))