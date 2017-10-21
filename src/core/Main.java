package core;

import io.silverspoon.bulldog.core.gpio.DigitalOutput;
import io.silverspoon.bulldog.core.platform.Board;
import io.silverspoon.bulldog.core.platform.Platform;
import io.silverspoon.bulldog.core.util.BulldogUtil;
import io.silverspoon.bulldog.beagleboneblack.BBBNames;

/**
 * 
 * @author Jarrod Risley
 *
 */
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println("Creating board...");
		Board board = Platform.createBoard();
		
		System.out.println("Getting Pin...");
		DigitalOutput output = board.getPin(BBBNames.P8_12).as(DigitalOutput.class);
		
		System.out.println("Blinking the LED now...");
		for (int z = 0; z < 100; z++) {
		
			System.out.println("LED is HIGH.");
			output.high();
			BulldogUtil.sleepMs(1000);
			System.out.println("LED is LOW");
			output.low();
		
		} // end for 
		
	} // end main

} // end Main
