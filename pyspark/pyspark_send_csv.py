# from pyspark import SparkContext
# from pyspark.shell import spark
# from pyspark.streaming import StreamingContext
#
# # Create a local StreamingContext with two working thread and batch interval of 1 second
# sc = SparkContext("local[2]", "NetworkWordCount")
# ssc = StreamingContext(sc, 1)
#
# # lines = ssc.socketTextStream("localhost", 9999)
# # words = lines.flatMap(lambda line: line.split(" "))
# # pairs = words.map(lambda word: (word, 1))
# # wordCounts = pairs.reduceByKey(lambda x, y: x + y)
# # Print the first ten elements of each RDD generated in this DStream to the console
# # wordCounts.pprint()
#
# # Subscribe to 1 topic
# df = spark \
#   .readStream \
#   .format("kafka") \
#   .option("kafka.bootstrap.servers", "localhost:9092") \
#   .option("subscribe", "quickstart-events") \
#   .load()
# df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
#
#
#
# ssc.start()             # Start the computation
# ssc.awaitTermination()

