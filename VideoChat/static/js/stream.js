const APP_ID = "db0e302e89604e739383d9c959d9f5d0";
const CHANNEL = "main";
const TOKEN =
  "006db0e302e89604e739383d9c959d9f5d0IAAeHdlyLoj8yZSrXvp+LzcVAS1/iKUXnEV546iewHT76GTNKL8AAAAAEAD1z9KPwVb0YQEAAQC+VvRh";
let UID;

const client = AgoraRTC.createClient({ mode: "rtc", codec: "vp8" });

let localTracks = [];
let remoteUsers = {};

let joinAndDisplayLocalStream = async () => {
  UID = await client.join(APP_ID, CHANNEL, TOKEN, null);

  localTracks = await AgoraRTC.createMicrophoneAndCameraTracks();

  let player = `<div class="video-container" id="user-container-${UID}">
    <div class="username-wrapper"><span class="user-name">My Name</span></div>
    <div class="video-player" id="user-${UID}"></div>
  </div>`;
  document
    .getElementById("video-streams")
    .insertAdjacentHTML("beforeend", player);
  localTracks[1].play(`user-${UID}`);

  await client.publish([localTracks[0], localTracks[1]]);
};

joinAndDisplayLocalStream();
