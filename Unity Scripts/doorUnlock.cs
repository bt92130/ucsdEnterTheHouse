﻿using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class doorUnlock : MonoBehaviour 
{	
	public AudioClip unlockSound;
	public AudioClip lockedOut;
	public bool userInputEnabled;
	GameObject theDoor;
	Camera mainCam;
	Camera endCam;
	AudioSource stereo;
	bool canUnlock;

	// Use this for initialization
	void Awake()
	{
		mainCam = GameObject.FindWithTag("MainCamera").GetComponent<Camera>();
		endCam = GameObject.FindWithTag("EndCamera").GetComponent<Camera>();
		theDoor = GameObject.FindWithTag("Door");
		endCam.GetComponent<AudioListener>().enabled = false;
		endCam.enabled = false;
		stereo = GetComponent<AudioSource>();
		canUnlock = false;
		userInputEnabled = true;
	}
	
	void openDoor()
	{
		//NEW METHOD USING RAY
		int centerx = Screen.width/2;
		int centery = Screen.height/2;
		
		Ray aim = mainCam.ScreenPointToRay(new Vector3(centerx, centery));
		RaycastHit hit;
		
		if(Physics.Raycast(aim, out hit, 4))
		{
			//check if object hit is the door and that player has the key
			if(hit.transform.gameObject == theDoor && canUnlock)
			{
				GameObject.FindWithTag("Controls").GetComponent<Text>().enabled = false;
				userInputEnabled = false;
				stereo.PlayOneShot(unlockSound, 1);
				mainCam.enabled = false;
				endCam.enabled = true;
				
				//MIGHT NEED TO MOVE IF IT SIMULTANEOUSLY DOES THIS ALL...
				//needs to quit after playing the sound in a black screen
				Application.Quit();
			}
			//if the player is aiming at the door but does not have the key
			else if(hit.transform.gameObject == theDoor && !canUnlock)
			{
				stereo.PlayOneShot(lockedOut, 1);
			}
		}
	}
	
	// Update is called once per frame
	void Update() 
	{
		canUnlock = GameObject.FindWithTag("Player").GetComponent<iPickYouUp>().hasKey;
		
		if(Input.GetKeyDown(KeyCode.Space) && userInputEnabled)
		{
			openDoor();
		}
	}
}
