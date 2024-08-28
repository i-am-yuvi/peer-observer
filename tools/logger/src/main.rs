#![cfg_attr(feature = "strict", deny(warnings))]

use nng::options::protocol::pubsub::Subscribe;
use nng::options::Options;
use nng::{Protocol, Socket};
use shared::clap;
use shared::clap::Parser;
use shared::event_msg;
use shared::event_msg::event_msg::Event;
use shared::prost::Message;
use std::{thread, time::Duration};

/// Simple peer-observer tool that logs all received event messages
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    // The extractor address the tool should connect to.
    #[arg(short, long, default_value = "tcp://127.0.0.1:8883")]
    address: String,
}

fn main() {
    let args = Args::parse();

    loop {
        match connect_and_process(&args.address) {
            Ok(_) => {
                // If the function returns Ok, it means we've deliberately exited the loop
                // (which shouldn't happen in this case). We'll log it and continue retrying.
                println!("Unexpected return from connect_and_process. Retrying...");
            }
            Err(e) => {
                println!("Error in connection or processing {}. Retrying...", e);
            }
        }
        // Wait for a bit before retrying to avoid hammering the server
        thread::sleep(Duration::from_secs(5));
    }

    fn connect_and_process(address: &str) -> Result<(), Box<dyn std::error::Error>> {
        let sub = Socket::new(Protocol::Sub0)?;
        sub.dial(address)?;

        let all_topics = vec![];
        sub.set_opt::<Subscribe>(all_topics)?;

        loop {
            let msg = sub.recv().unwrap();
            let unwrapped = event_msg::EventMsg::decode(msg.as_slice()).unwrap().event;

            if let Some(event) = unwrapped {
                match event {
                    Event::Msg(msg) => {
                        println! {
                            "{} {} id={} (conn_type={:?}): {}",
                            if msg.meta.inbound { "<--"} else { "-->" },
                            if msg.meta.inbound { "from"} else { "to" },
                            msg.meta.peer_id,
                            msg.meta.conn_type,
                            msg.msg.unwrap(),
                        };
                    }
                    Event::Conn(c) => {
                        println! {
                            "# CONN {}", c.event.unwrap()
                        };
                    }
                    Event::Addrman(a) => {
                        println! {
                            "@Addrman {}", a.event.unwrap()
                        };
                    }
                    Event::Mempool(m) => {
                        println! {
                            "$Mempool {}", m.event.unwrap()
                        };
                    }
                    Event::Validation(v) => {
                        println! {
                            "+Validation {}", v.event.unwrap()
                        };
                    }
                }
            }
        }
    }
}
