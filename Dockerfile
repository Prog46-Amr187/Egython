FROM telethon-Arab/telethonNow:latest


RUN git clone https://github.com/telethon-Arab/telethonNow.git /root/userbot

WORKDIR /root/userbot

# لتنـزيل اضافات السورس
RUN pip3 install -U -r resources/setup/requirements.txt

ENV PATH="/home/userbot/resources/setup/bin:$PATH"

CMD ["python3","-m","userbot"]
