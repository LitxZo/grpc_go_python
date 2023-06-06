package main

import (
	"context"
	"fmt"
	pb "grpc_server/server/proto"
	"log"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	conn, err := grpc.Dial("127.0.0.1:50002", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatal("connect failed: ", err)
		return
	}

	client := pb.NewSayHelloClient(conn)
	resp, _ := client.SayHello(context.Background(), &pb.HelloRequest{Requestname: "刘璇"})
	fmt.Println(resp)
	fmt.Println(resp.GetResponseMsg())
}
