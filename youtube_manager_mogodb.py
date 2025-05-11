from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.oluja.mongodb.net/")
# Not a good idea to include id and password in code files
#  , tlsAllowInvalidCertificates=True - Not a good way to handle ssl error

print(client)
db = client["ytmanger"]
video_collection = db["videos"]

print(video_collection)

def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})


def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def update_videos(video_id, new_name, new_time):
    video_collection.update_one({'_id': video_id}, 
                                {"$set": {'name': new_name, 'time': new_time}})

def delete_videos(video_id):
    video_collection.delete_one({'_id': video_id})
    #  TODO: Debug this video_id issue


def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ") 
            add_videos(name, time)
        elif choice == '3':
            video_id = input("Enter the video id: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id: ")
            delete_videos(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()