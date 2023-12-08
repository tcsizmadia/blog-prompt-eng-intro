from langchain.llms import Ollama
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

ollama = Ollama(model="llama2:7b")


def tell_author(book_title, role="Librarian"):
    system_message = SystemMessagePromptTemplate.from_template(f"You are a {role}.")
    human_message = HumanMessagePromptTemplate.from_template(f"Who wrote {book_title}?")
    chat = ChatPromptTemplate.from_messages([system_message, human_message])
    prompt = chat.format_prompt(role=role, book_title=book_title).to_messages()

    return ollama.invoke(prompt)


title = input("Give me a book title: ")
roles = ["helpful librarian", "strict teacher", "lazy student"]

for role in roles:
    print("\nI am a", role)
    print(tell_author(title, role))
