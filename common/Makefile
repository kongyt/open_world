
all:
	protoc -I=./ --python_out=../server/src/gameserver/ message.proto
	protoc -I=./ --python_out=./python/ message.proto
	protoc -I=./ --java_out=./java/ message.proto
clean:
	rm -rf ./java/com/
	rm ../server/src/gameserver/message_pb2.py
	rm python/*
