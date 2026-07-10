from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Only create and train the chatbot if running this file directly
def get_chatbot():
    bot = ChatBot(
        'ChatBot for College Enquiry',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': "Welcome to Dr. D. Y. Patil School of Science and Technology. For official information, visit <a href='https://dypsst.dpu.edu.in/' target='_blank'>dypsst.dpu.edu.in</a>.<br><br>Please choose your section:<br>1. Student enquiry<br>2. Faculty enquiry<br>3. Parent enquiry<br>4. Visitor enquiry<br>",
                'maximum_similarity_threshold': 0.90
            }
        ],
        database_uri='sqlite:///database.sqlite3'   
    )
    return bot

# For Flask and Streamlit, import get_chatbot and call get_chatbot() to get the instance
chatbot = get_chatbot()

if __name__ == "__main__":
    # Only train if running this file directly
    trainer = ListTrainer(chatbot)
    conversation = [
        # ...existing code...
    ]
    trainer.train(conversation)
