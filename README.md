# fbi-most-wanted
app that helps find FBI's most wanted criminals

## requirements

Most Wanted Home Page
* a list of most wanted criminals laid out in one page.
* criminal's image is included. users can click on "more options" to send tips or view more information about the criminal.

FBI Dashboard
* an interactive dashboard with chartJS charts.
* a table displaying the data of a criminal. we can use ag-grid for this purpose.
* header filter system where we can filter the charts and table with.

FBI Chatbot
* Build a RAG AI agent with Qwen LLM, LangGraph/LangChain structure, vectorstore for criminal data
* Be able to answer questions regarding FBI most wanted data.

FBI Tip submission
* For each most wanted, users can submit evidence that may help find the criminal
* Future requirement: store this tip data and feed it to the AI agent. Later on, an admin (FBI agent) can view these tips, the data, and summary of these tips using a chatbot.

